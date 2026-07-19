def commands(binary_str):

    actions = [
    "wink",
    "double blink",
    "close your eyes",
    "jump",
    ]
    
    action_list= []

    for i,value in enumerate(reversed(binary_str)):
        if value == "1":
            if i < 4:
                action_list.append(actions[i])
            else:
                action_list.reverse()
        
    return action_list
        
        
    
