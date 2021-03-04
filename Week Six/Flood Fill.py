class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        val = image[sr][sc]
        image[sr][sc] = newColor
        print(sr, sc)
        if val == newColor:
            return image

        if sr >= 1:
            if image[sr-1][sc] == val:
                self.floodFill(image, sr-1, sc, newColor)

        if sr+1 < len(image):
            if image[sr+1][sc] == val:
                self.floodFill(image, sr+1, sc, newColor)

        if sc >= 1:
            if image[sr][sc-1] == val:
                self.floodFill(image, sr, sc-1, newColor)

        if sc + 1 < len(image[0]):
            if image[sr][sc+1] == val:
                self.floodFill(image, sr, sc+1, newColor)

        return image
