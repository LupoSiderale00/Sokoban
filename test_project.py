# test_project.py

import os
from project import get_player_pos, find_target, open_level, level_global, target_pos

def test_get_player_pos():
    # Set up the board
    level_global.clear()
    level_global.extend([
        ["#", "#", "#"],
        ["#", "@", "#"],
        ["#", " ", "#"]
    ])
    assert get_player_pos() == (1, 1)

def test_find_target():
    # Set up the board with a target
    level_global.clear()
    target_pos.clear()
    level_global.extend([
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", "@", "#"]
    ])
    find_target()
    assert target_pos == ["1,1"]

def test_open_level(tmp_path):
    # Create a temp file to simulate a level file
    level_text = "###\n#@$\n###\n"
    level_file = tmp_path / "level1.txt"
    level_file.write_text(level_text)

    # Simulate selecting "easy" mode and renaming the file to match logic
    real_path = tmp_path / "level1current.txt"
    os.rename(level_file, tmp_path / "level1.txt")

    # Patch project.py to use the file we just created
    os.chdir(tmp_path)  # temporarily change working directory
    level_global.clear()
    result = open_level("e")
    os.chdir("..")  # reset working directory back

    assert isinstance(result, list)
    assert result[0] == "###\n"
    assert level_global[1][1] == "@"
