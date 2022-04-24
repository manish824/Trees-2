# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root==None :return 0
        s=[]
        s1=[]
        sum1=0
        num=0
        while(root!=None or len(s)!=0):
            while(root!=None):
                s.append(root)
                num=num*10+root.val
                s1.append(num)
                root=root.left
            root=s.pop()
            num=s1.pop()
            if(root.left == None and root.right==None):
                sum1=sum1+num
            root=root.right
        return sum1
        