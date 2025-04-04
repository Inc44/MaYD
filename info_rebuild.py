import argparse
from os import listdir, path, remove
from info import read_info


def parse_arguments():
	parser = argparse.ArgumentParser(
		description="Modify database, rebuild playlist, and remove audio files"
	)
	parser.add_argument("database_path", type=str, help="Path to the database file")
	parser.add_argument("playlist_path", type=str, help="Path to the playlist file")
	parser.add_argument("input_dir", type=str, help="Directory containing audio files")
	return parser.parse_args()


def print_menu():
	print("\nOptions:")
	print("Enter ID(s) to remove (space-separated)")
	print("Enter '1' to write changes to the database")
	print("Enter '2' to remove audio files")
	print("Enter '3' to exit")


def write_info_list(info_list, database_path="main.database"):
	lines = [
		"%(id)s\t%(title)s\t%(upload_date)s\t%(artist)s\t%(album)s\t%(track)s\t%(release_year)s"
		% entry
		for entry in info_list
	]
	with open(database_path, "w", encoding="utf-8") as f:
		f.write("\n".join(lines) + "\n")
	return database_path


def playlist_info_list(info_list, playlist_path="main.playlist"):
	ids = []
	for entry in info_list:
		id = entry.get("id")
		ids.append(id)
	with open(playlist_path, "w", encoding="utf-8") as f:
		for id in range(0, len(ids), 50):
			playlist_chunk = ids[id : id + 50]
			playlist_link = (
				f"www.youtube.com/watch_videos?video_ids={','.join(playlist_chunk)}"
			)
			f.write(playlist_link + "\n")
	return playlist_path


def remove_info_list(info_list, ids_to_remove):
	return [entry for entry in info_list if entry.get("id") not in ids_to_remove]


def remove_files(input_dir, ids_to_remove):
	file_names = []
	for file_name in listdir(input_dir):
		for id_to_remove in ids_to_remove:
			if f"[{id_to_remove}]" in file_name:
				file_path = path.join(input_dir, file_name)
				remove(file_path)
				file_names.append(file_path)
				break
	return file_names


def main():
	arguments = parse_arguments()
	info_list = read_info(arguments.database_path)
	print(f"Loaded database with {len(info_list)} entries")
	changes_made = False
	ids_to_remove = set()
	while True:
		print_menu()
		user_input = input("Enter your choice: ").strip()
		if user_input == "1":
			if changes_made:
				current_info_list = remove_info_list(info_list, ids_to_remove)
				write_info_list(current_info_list, arguments.database_path)
				playlist_info_list(current_info_list, arguments.playlist_path)
				print(
					f"Changes saved. Removed {len(info_list) - len(current_info_list)} entries from the database."
				)
				print(
					f"Database and playlist rebuilt. New database size: {len(current_info_list)} entries."
				)
				info_list = current_info_list
				changes_made = False
			else:
				print("No changes were made.")
		elif user_input == "2":
			if ids_to_remove:
				file_names = remove_files(arguments.input_dir, ids_to_remove)
				print(f"Removed {len(file_names)} audio files.")
				for file_name in file_names:
					print(f"Removed: {file_name}")
			else:
				print("No IDs specified for removal. Please enter IDs first.")
		elif user_input == "3":
			if changes_made:
				confirm = input(
					"Are you sure you want to exit without saving changes to the database? (y/n): "
				).lower()
				if confirm == "y":
					print("Exiting without saving changes to the database.")
					break
				else:
					continue
			else:
				print("Exiting.")
				break
		else:
			new_ids_to_remove = set(user_input.split())
			ids_to_remove.update(new_ids_to_remove)
			changes_made = True
			print(
				f"Added {len(new_ids_to_remove)} IDs to the removal list. Total IDs to remove: {len(ids_to_remove)}"
			)


if __name__ == "__main__":
	main()
