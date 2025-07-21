import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox
from PyQt6.QtGui import QColor
import solver

class PentominoGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pentomino Solver')
        self.GRID_WIDTH = solver.GRID_WIDTH
        self.GRID_HEIGHT = solver.GRID_HEIGHT
        self.CELL_SIZE = 50
        self.grid_buttons = []
        self.blocked_cells = []
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()
        self.layout.setSpacing(2)

        for r in range(self.GRID_HEIGHT):
            row_buttons = []
            for c in range(self.GRID_WIDTH):
                button = QPushButton()
                button.setFixedSize(self.CELL_SIZE, self.CELL_SIZE)
                button.setStyleSheet("background-color: white; border: 1px solid gray")
                button.clicked.connect(lambda _, r=r, c=c: self.grid_click(r, c))
                self.layout.addWidget(button, r, c)
                row_buttons.append(button)
            self.grid_buttons.append(row_buttons)

        self.solve_button = QPushButton('Solve')
        self.solve_button.clicked.connect(self.solve_puzzle)
        self.layout.addWidget(self.solve_button, self.GRID_HEIGHT, 0, 1, self.GRID_WIDTH // 2)

        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.reset_puzzle)
        self.layout.addWidget(self.reset_button, self.GRID_HEIGHT, self.GRID_WIDTH // 2, 1, self.GRID_WIDTH // 2)

        self.setLayout(self.layout)

    def grid_click(self, r, c):
        if (r, c) in self.blocked_cells:
            self.blocked_cells.remove((r, c))
            self.grid_buttons[r][c].setStyleSheet("background-color: white; border: 1px solid gray")
        elif len(self.blocked_cells) < 3:
            self.blocked_cells.append((r, c))
            self.grid_buttons[r][c].setStyleSheet("background-color: black; border: 1px solid gray")

    def solve_puzzle(self):
        if len(self.blocked_cells) != 3:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Please select exactly 3 blocked cells.")
            msg.setWindowTitle("Error")
            msg.exec()
            return

        board = [[0 for _ in range(self.GRID_WIDTH)] for _ in range(self.GRID_HEIGHT)]
        for r, c in self.blocked_cells:
            board[r][c] = -1

        solution = solver.solve(board, solver.ALL_PIECES)

        if solution:
            self.draw_solution(solution)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("No solution found.")
            msg.setWindowTitle("Solver")
            msg.exec()

    def draw_solution(self, board):
        colors = ["#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4", "#42d4f4", "#f032e6", "#bfef45", "#fabed4", "#469990", "#dcbeff"]
        for r in range(self.GRID_HEIGHT):
            for c in range(self.GRID_WIDTH):
                piece_id = board[r][c]
                if piece_id == -1:
                    color = "black"
                elif piece_id > 0:
                    color = colors[piece_id % len(colors)]
                else:
                    color = "white"
                self.grid_buttons[r][c].setStyleSheet(f"background-color: {color}; border: 1px solid gray")

    def reset_puzzle(self):
        self.blocked_cells = []
        for r in range(self.GRID_HEIGHT):
            for c in range(self.GRID_WIDTH):
                self.grid_buttons[r][c].setStyleSheet("background-color: white; border: 1px solid gray")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PentominoGUI()
    ex.show()
    sys.exit(app.exec())