from todolist import TodoList

todo = TodoList()
    
    # Add tasks
todo.add("Buy groceries")
todo.add("Read Python book")
todo.add("Call Alice")

# Complete one task
todo.complete(2)

# List tasks
todo.list_all()
todo.list_pending()
todo.list_done()

# Remove a task
todo.remove(1)
todo.list_all()