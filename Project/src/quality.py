import chess
import chess.engine
import json
import pandas as pd
from tqdm import tqdm

# Stockfish setup
STOCKFISH_PATH = "/opt/homebrew/bin/stockfish"

# Load JSON data
def load_json_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Analyze a single game
def analyze_game(game_data, engine):
    moves = game_data["Moves"].split(" ")
    white_elo = int(game_data["WhiteElo"])
    black_elo = int(game_data["BlackElo"])

    board = chess.Board()
    move_qualities = {"good": 0, "inaccuracy": 0, "mistake": 0, "blunder": 0}

    # Analyze moves
    for move in moves:
        try:
            board.push_san(move)
            info = engine.analyse(board, chess.engine.Limit(depth=10))
            eval_cp = info["score"].relative.score(mate_score=10000)

            # Classify move quality
            if eval_cp is not None:
                eval_change = abs(eval_cp / 100)
                if eval_change < 0.2:
                    move_qualities["good"] += 1
                elif eval_change < 1.0:
                    move_qualities["inaccuracy"] += 1
                elif eval_change < 3.0:
                    move_qualities["mistake"] += 1
                else:
                    move_qualities["blunder"] += 1
        except Exception as e:
            continue

    return white_elo, black_elo, move_qualities, game_data["GameMode"]

# Main analysis
def analyze_quality_of_movements(json_files, output_csv, games_per_dataset=500):
    results = []
    with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
        for file_path in json_files:
            data = load_json_data(file_path)
            
            # Limit to the specified number of games
            game_count = 0  # Counter to track processed games
            
            for game_data in tqdm(data):
                if game_count >= games_per_dataset:
                    break  # Stop after reaching the limit
                
                white_elo, black_elo, move_qualities, game_mode = analyze_game(game_data, engine)
                results.append({
                    "WhiteElo": white_elo,
                    "BlackElo": black_elo,
                    "GameMode": game_mode,
                    **move_qualities
                })
                game_count += 1  # Increment counter

    # Save results to a CSV for further analysis
    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")

# Execute analysis
if __name__ == "__main__":
    json_files = [
        "../datasets/processed/JSON/October-2024_chunk_1.json",
        "../datasets/processed/JSON/October-2024_chunk_2.json",
        "../datasets/processed/JSON/October-2024_chunk_3.json",
        "../datasets/processed/JSON/October-2024_chunk_4.json",
        "../datasets/processed/JSON/October-2024_chunk_5.json"
    ]
    output_csv = "../results/quality_of_moves.csv"
    analyze_quality_of_movements(json_files, output_csv)