import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import random
import heapq

SIZE = 3
TILE_SIZE = 120
GOAL = (0, 1, 2, 3, 4, 5, 6, 7, 8)


class ImagePuzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Puzzle – Image Version")
        self.root.resizable(False, False)

        self.tiles = []
        self.images = []
        self.buttons = []
        self.moves = 0

        self.pick_image()
        self.create_ui()
        self.shuffle()

    # ---------- IMAGE ----------
    def pick_image(self):
        file = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Images", "*.png *.jpg *.jpeg")]
        )
        if not file:
            self.root.destroy()
            return

        img = Image.open(file)

        # auto center-crop to square
        w, h = img.size
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 2
        img = img.crop((left, top, left + side, top + side))
        img = img.resize((SIZE * TILE_SIZE, SIZE * TILE_SIZE))

        self.images = [None]  # index 0 = blank
        for i in range(1, SIZE * SIZE):
            r, c = divmod(i, SIZE)
            tile = img.crop((
                c * TILE_SIZE,
                r * TILE_SIZE,
                (c + 1) * TILE_SIZE,
                (r + 1) * TILE_SIZE
            ))
            self.images.append(ImageTk.PhotoImage(tile))

    # ---------- UI ----------
    def create_ui(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack()

        for i in range(9):
            btn = tk.Button(
                frame,
                command=lambda i=i: self.move(i),
                borderwidth=1,
                relief="solid",
                padx=0,
                pady=0
            )
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

        self.status = tk.Label(self.root, text="Moves: 0")
        self.status.pack(pady=5)

        tk.Button(self.root, text="Hint (Shortest Move)",
                  command=self.hint).pack()

        tk.Button(self.root, text="New Game",
                  command=self.shuffle).pack(pady=5)

    # ---------- GAME ----------
    def shuffle(self):
        nums = list(range(9))
        while True:
            random.shuffle(nums)
            if self.solvable(nums) and tuple(nums) != GOAL:
                break
        self.tiles = nums
        self.moves = 0
        self.update()

    def update(self):
        for i, v in enumerate(self.tiles):
            if v == 0:
                self.buttons[i].config(
                    image="",
                    bg="gray",
                    state="disabled"
                )
            else:
                self.buttons[i].config(
                    image=self.images[v],
                    bg="SystemButtonFace",
                    state="normal"
                )
        self.status.config(text=f"Moves: {self.moves}")

    def move(self, i):
        z = self.tiles.index(0)
        if self.adjacent(i, z):
            self.tiles[z], self.tiles[i] = self.tiles[i], self.tiles[z]
            self.moves += 1
            self.update()

            if tuple(self.tiles) == GOAL:
                messagebox.showinfo("Solved 🎉",
                                    f"Solved in {self.moves} moves!")

    def adjacent(self, a, b):
        ra, ca = divmod(a, 3)
        rb, cb = divmod(b, 3)
        return abs(ra - rb) + abs(ca - cb) == 1

    def solvable(self, board):
        inv = 0
        nums = [x for x in board if x != 0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    inv += 1
        return inv % 2 == 0

    # ---------- A* HINT ----------
    def hint(self):
        path = self.astar(tuple(self.tiles))
        if path and len(path) > 1:
            self.tiles = list(path[1])
            self.moves += 1
            self.update()

    def astar(self, start):
        pq = [(0, start)]
        g = {start: 0}
        parent = {start: None}

        while pq:
            _, cur = heapq.heappop(pq)
            if cur == GOAL:
                return self.reconstruct(parent, cur)

            for n in self.neighbors(cur):
                t = g[cur] + 1
                if n not in g or t < g[n]:
                    g[n] = t
                    f = t + self.manhattan(n)
                    heapq.heappush(pq, (f, n))
                    parent[n] = cur
        return None

    def reconstruct(self, parent, cur):
        path = [cur]
        while parent[cur]:
            cur = parent[cur]
            path.append(cur)
        return path[::-1]

    def neighbors(self, s):
        z = s.index(0)
        r, c = divmod(z, 3)
        res = []
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                lst = list(s)
                lst[z], lst[nz] = lst[nz], lst[z]
                res.append(tuple(lst))
        return res

    def manhattan(self, s):
        d = 0
        for i, v in enumerate(s):
            if v == 0:
                continue
            gi = GOAL.index(v)
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(gi, 3)
            d += abs(r1 - r2) + abs(c1 - c2)
        return d


if __name__ == "__main__":
    root = tk.Tk()
    ImagePuzzle(root)
    root.mainloop()
    