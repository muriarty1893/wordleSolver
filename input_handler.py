def get_user_input():
    pattern = input("Word pattern (e.g., '_a___'): ").strip()
    must_include = set(input("Must include letters (e.g., 'as'): ").strip())
    must_not_include = set(input("Must not include letters (e.g., 'zqx'): ").strip())
    excluded_positions = {}
    while True:
        letter = input("Letter to exclude position (Enter to finish): ").strip()
        if not letter:
            break
        positions = input(f"Positions where {letter} should not be (e.g., '1,3'): ").strip()
        excluded_positions[letter] = [int(pos) - 1 for pos in positions.split(',') if pos.isdigit()]
    return pattern, must_include, must_not_include, excluded_positions