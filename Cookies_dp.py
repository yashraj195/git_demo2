"""class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        l=0
        r=0
        while (l<m and r<n):
            if (g[r]<=s[l]):
                r=r+1
            l=l+1
        return r


g=[2,4,3,1]
s=[4,2,6,3,2]
solution = Solution()
re = solution.findContentChildren(g, s)
print(re)
"""

def find_leaders(arr):
    size = len(arr)
    for i in range(size):
        for j in range(i + 1, size):
            if arr[i] <= arr[j]:
                break
        else:  # This 'else' corresponds to the 'for', not 'if'
            print(arr[i], end=" ")

def main():
    print("Enter the length of the array:")
    length = int(input())
    arr = []
    print("Enter the elements of the array:")
    for _ in range(length):
        arr.append(int(input()))
    
    find_leaders(arr)

if __name__ == "__main__":
    main()
