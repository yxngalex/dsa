def _display(node):
    if node is None:
        return "", 0, 0, 0

    line = str(node.value)
    width = len(line)

    if node.left is None and node.right is None:
        return line, width, 1, width // 2

    if node.left is None:
        right_str, right_width, right_height, right_middle = _display(node.right)
        first_line = line + " " * (right_width + 1)
        second_line = " " * len(line) + "\\" + " " * right_width
        shifted_right = [(" " * len(line)) + rline for rline in right_str.split("\n")]
        return "\n".join(
            [first_line, second_line] + shifted_right), width + right_width + 1, right_height + 2, width // 2

    if node.right is None:
        left_str, left_width, left_height, left_middle = _display(node.left)
        first_line = " " * (left_width + 1) + line
        second_line = " " * (left_middle + 1) + "/" + " " * (left_width - left_middle - 1 + len(line))
        shifted_left = [l + (" " * len(line)) for l in left_str.split("\n")]
        return "\n".join(
            [first_line, second_line] + shifted_left), left_width + width + 1, left_height + 2, left_width + width // 2

    left_str, left_width, left_height, left_middle = _display(node.left)
    right_str, right_width, right_height, right_middle = _display(node.right)
    first_line = " " * (left_width + 1) + line + " " * (right_width + 1)
    second_line = " " * (left_middle + 1) + "/" + " " * (left_width - left_middle - 1 + len(line) + right_middle) + "\\"

    left_lines = left_str.split("\n")
    right_lines = right_str.split("\n")
    if left_height < right_height:
        left_lines += [" " * left_width] * (right_height - left_height)
    elif right_height < left_height:
        right_lines += [" " * right_width] * (left_height - right_height)

    combined_lines = [l + (" " * len(line)) + r for l, r in zip(left_lines, right_lines)]
    return "\n".join([first_line, second_line] + combined_lines), left_width + width + right_width + 2, max(left_height,
                                                                                                            right_height) + 2, left_width + width // 2


def display(node):
    result, *_ = _display(node)
    return result
