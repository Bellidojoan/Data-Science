import chess.pgn
import json
from threading import Thread
import os

# Function to classify game mode based on TimeControl
def classify_game_mode(time_control):
    """
    Classify game mode based on time control.
    Bullet: Total time <= 3 minutes
    Blitz: Total time <= 10 minutes
    Rapid: Total time <= 25 minutes
    Classical: Total time > 25 minutes
    """
    try:
        base, increment = map(int, time_control.split("+"))
        total_time = base + increment  # Base time in seconds + increment
    except ValueError:
        return "Unknown"  # Handle missing or invalid time controls

    if total_time <= 180:
        return "Bullet"
    elif total_time <= 600:
        return "Blitz"
    elif total_time <= 1500:
        return "Rapid"
    else:
        return "Classical"

# Function to parse PGN file and extract data for a chunk of games
def parse_pgn_chunk(pgn_file, start_index, chunk_size, output_file):
    games_data = []
    with open(pgn_file, 'r') as pgn:
        # Skip games until the starting index
        for _ in range(start_index):
            game = chess.pgn.read_game(pgn)
            if game is None:
                break

        # Parse the required chunk of games
        count = 0
        while count < chunk_size:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break

            # Extracting relevant game information
            game_data = {
                "Date": game.headers.get("Date", "Unknown"),
                "ECO": game.headers.get("ECO", "Unknown"),
                "Opening": game.headers.get("Opening", "Unknown"),
                "TimeControl": game.headers.get("TimeControl", "Unknown"),
                "Termination": game.headers.get("Termination", "Unknown"),
                "Result": game.headers.get("Result", "Unknown"),
                "Moves": game.board().variation_san(game.mainline_moves()),
                "WhiteElo": game.headers.get("WhiteElo", "Unknown"),
                "BlackElo": game.headers.get("BlackElo", "Unknown"),
            }
            # Add GameMode classification
            game_data["GameMode"] = classify_game_mode(game_data["TimeControl"])
            games_data.append(game_data)
            count += 1

    # Save chunk to JSON
    save_to_json(games_data, output_file)

# Function to save data to a JSON file
def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)
    print(f"Data successfully saved to {output_file}")

# Main execution
if __name__ == "__main__":
    input_file = "../datasets/raw/October-2024.pgn"
    chunk_size = 100000
    num_threads = 5  # Adjust based on the number of cores or desired splits

    threads = []
    for i in range(num_threads):
        start_index = i * chunk_size
        output_file = f"../datasets/processed/JSON/October-2024_chunk_{i+1}.json"
        
        # Create a thread for each chunk
        thread = Thread(target=parse_pgn_chunk, args=(input_file, start_index, chunk_size, output_file))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All chunks processed and saved.")