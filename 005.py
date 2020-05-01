# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#从尾到头打印链表
def PrintListReversingly_Iteratively(pHead):
    nodes = []
    pNode = pHead
    while pHead != None:
        nodes.append(pNode.val)
        pNode = pNode.next
    while not nodes:
        pNode = nodes.pop()
        print(pNode)

def PrintListReversingly_recursively(pHead):
    if pHead != None:
        if pHead.next != None:
            PrintListReversingly_recursively(pHead.next)
        print(pHead.val)
