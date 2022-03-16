# First, we need to initialise 3 variables. The first one will be holding the carry will be forwarding over at each step, the second one will be a Linked List that will represent the final result (initially set to value 0) and the third one will be our pointer that will be using in order to move towards the next node at every iteration.

carry = 0
result = ListNode(0)
pointer = result


# # in pointer will have an immediate effect on result as well as both of these variables are sharing the same object reference.
# Now that we have initialised these variables we can start iterating over the linked lists. Essentially, we need to keep iterating until there are no more nodes in either of the lists and when we don’t carry over any additional unit. Therefore, a while loop with the conditions shown below should do the trick:
while (l1 or l2 or carry):
    first_num = l1.val if l1.val else 0
    second_num = l2.val if l2.val else 0    # Then we need to retrieve the digits from the individual nodes. Since the linked lists could be of different size (or even reach the end of both lists but still carrying over a unit) we also need to handle the cases where the value of the node is None.
    
    summation = first_num + second_num + carry
    num = summation % 10
    carry = summation // 10     #Then we need to perform the addition and see whether this will have any impact. To do so, we first add together the two numbers as well as the carry. Then we compute the next digit of the solution by taking the modulo between the sum and number 10 and then carry by performing a floor division between the sum and number 10 .
                                #For instance, if the sum of the two digits is 12, num variable will be set to 2 (because 12 % 10 = 2) and carry will be 1 (since 12 // 10 = 1).
   
    pointer.next = ListNode(num)
                                    # Finally, we store the result to the pointer (that will also update result since these two variables are sharing the reference to the same object) and the move the pointer to the next node (if any):
    pointer = pointer.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None  
    
    
return result.next