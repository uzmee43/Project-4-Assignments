import tkinter as tk

# Grid settings
ROWS = 10
COLS = 10
CELL_SIZE = 40
ERASER_SIZE = 60

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
        self.canvas.pack()
        self.cells = {}

        # Draw blue grid
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                self.cells[(row, col)] = rect

        # Create eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray", outline="black")
        self.canvas.tag_bind(self.eraser, "<B1-Motion>", self.move_eraser)
        self.canvas.bind("<B1-Motion>", self.move_eraser)  # Allow dragging anywhere

    def move_eraser(self, event):
        # Move eraser to mouse position
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Erase cells that intersect with eraser
        for (row, col), rect in self.cells.items():
            rx1, ry1, rx2, ry2 = self.canvas.coords(rect)
            if self.rects_overlap(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
                self.canvas.itemconfig(rect, fill="white")

    @staticmethod
    def rects_overlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        return not (ax2 <= bx1 or ax1 >= bx2 or ay2 <= by1 or ay1 >= by2)

def main():
    root = tk.Tk()
    root.title("Eraser Canvas")
    EraserCanvas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
# Output: A window with a blue grid and a gray eraser that can be moved to erase the grid cells.
# The code creates a GUI application using Tkinter that allows the user to erase parts of a blue grid by dragging a gray eraser.