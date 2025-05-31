import random # Make sure random is imported at the top of the file
CELL_SIZE_METERS = 1.0

class GridLayout:
    def __init__(self, map_size: tuple[int, int], shelf_coordinates: list[tuple[int, int]], docking_stations: list[tuple[int, int]]):
        self.map_size_cells = map_size  # e.g., (100, 50) cells
        self.shelf_coordinates = shelf_coordinates
        self.docking_stations = docking_stations

        self.map_width_cells = map_size[0]
        self.map_height_cells = map_size[1]

        # Assuming CELL_SIZE_METERS is defined in this file, e.g., CELL_SIZE_METERS = 1.0
        self.map_width_meters = self.map_width_cells * CELL_SIZE_METERS
        self.map_height_meters = self.map_height_cells * CELL_SIZE_METERS

    # Keep other methods as stubs for now
    def random_free_cell(self) -> tuple[int, int]:
        """
        Returns a random cell (x, y) within the map boundaries.
        Currently, any cell not a boundary wall is considered free.
        This will need to be updated later when shelves/obstacles are introduced.
        Returns a tuple (x, y) of cell indices.
        """
        # For now, any cell not a wall is considered free.
        # This does not yet account for shelves or other obstacles.
        x = random.randint(0, self.map_width_cells - 1)
        y = random.randint(0, self.map_height_cells - 1)
        return (x, y)

    def is_wall(self, x: int, y: int) -> bool:
        """
        Checks if the given cell coordinates (x, y) are outside the map boundaries.
        x: cell index along the width
        y: cell index along the height
        Returns True if the cell is a wall (outside boundaries), False otherwise.
        """
        if x < 0 or x >= self.map_width_cells:
            return True
        if y < 0 or y >= self.map_height_cells:
            return True
        return False
