import tkinter as tk

class ChessboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chessboard")
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.create_chessboard()
    
    def create_chessboard(self):
        self.buttons = [[None for _ in range(8)] for _ in range(8)]

        for row in range(8):
            for col in range(8):
                color = 'white' if (row + col) % 2 == 0 else 'black'
                self.buttons[row][col] = tk.Button(self.root, text=self.board[row][col], width=5, height=2, bg=color, command=lambda r=row, c=col: self.on_square_click(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def on_square_click(self, row, col):
        piece = self.board[row][col]
        if piece == ' ':
            print(f"Empty square clicked: {chr(col + ord('A'))}{8 - row}")
        else:
            print(f"Piece {piece} clicked: {chr(col + ord('A'))}{8 - row}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessboardApp(root)
    root.mainloop()
