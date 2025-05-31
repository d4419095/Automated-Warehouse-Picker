import unittest
from warehouse_automation_ai.envs.grid_layout import GridLayout, CELL_SIZE_METERS

class TestGridLayout(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.map_size = (10, 20)  # 10 cells wide, 20 cells high
        self.shelf_coords = [(1, 1), (2, 2)]
        self.docking_stations = [(0, 0), (9, 19)]
        self.layout = GridLayout(
            map_size=self.map_size,
            shelf_coordinates=self.shelf_coords,
            docking_stations=self.docking_stations
        )

    def test_initialization(self):
        """Test GridLayout initialization and correct storage of dimensions."""
        self.assertEqual(self.layout.map_size_cells, self.map_size)
        self.assertEqual(self.layout.map_width_cells, self.map_size[0])
        self.assertEqual(self.layout.map_height_cells, self.map_size[1])
        self.assertEqual(self.layout.shelf_coordinates, self.shelf_coords)
        self.assertEqual(self.layout.docking_stations, self.docking_stations)

        expected_width_meters = self.map_size[0] * CELL_SIZE_METERS
        expected_height_meters = self.map_size[1] * CELL_SIZE_METERS
        self.assertEqual(self.layout.map_width_meters, expected_width_meters)
        self.assertEqual(self.layout.map_height_meters, expected_height_meters)

    def test_is_wall_boundary_conditions(self):
        """Test is_wall for boundary conditions."""
        # Test corners
        self.assertTrue(self.layout.is_wall(-1, 0))
        self.assertTrue(self.layout.is_wall(0, -1))
        self.assertTrue(self.layout.is_wall(self.map_size[0], 0))
        self.assertTrue(self.layout.is_wall(0, self.map_size[1]))
        self.assertTrue(self.layout.is_wall(self.map_size[0], self.map_size[1]))

        # Test just outside boundaries
        self.assertTrue(self.layout.is_wall(self.map_size[0], 5)) # x out of bounds
        self.assertTrue(self.layout.is_wall(5, self.map_size[1])) # y out of bounds

        # Test just inside boundaries
        self.assertFalse(self.layout.is_wall(0, 0))
        self.assertFalse(self.layout.is_wall(self.map_size[0] - 1, self.map_size[1] - 1))
        self.assertFalse(self.layout.is_wall(5, 5)) # A point well within bounds

    def test_random_free_cell_within_bounds(self):
        """Test random_free_cell to ensure it returns coordinates within bounds."""
        for _ in range(100): # Run a few times to increase confidence
            x, y = self.layout.random_free_cell()
            self.assertGreaterEqual(x, 0)
            self.assertLess(x, self.map_size[0])
            self.assertGreaterEqual(y, 0)
            self.assertLess(y, self.map_size[1])
            # Also ensure it's not a wall (though current random_free_cell doesn't explicitly check is_wall)
            self.assertFalse(self.layout.is_wall(x,y))

if __name__ == '__main__':
    unittest.main()
