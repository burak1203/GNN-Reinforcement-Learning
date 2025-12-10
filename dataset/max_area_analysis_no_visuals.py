def max_area(height: list[int]) -> int:
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that
    the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the         most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
    """
    left: int = 0
    right: int = len(height) - 1
    marea: int = 0

    while left < right:
        width: int = right - left
        shorter_height: int = min(height[left], height[right])
        current_area: int = width * shorter_height
        marea = max(marea, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return marea
