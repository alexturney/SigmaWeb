info = {
    "team":   "Carwash Demo",
    "members":   "Sanketh, Soroush, Pranava, and Nathan",
    "description":  
        """This is a simulation demo of the classic Carwash model. 
           I hope you enjoy!"""
}

sigma = {
    "model": "Car_Wash",    
    "parameters": [
        {   "name": "QUEUE",
            "display": "Initial Queue",
            "default": 0
        },

        {   "name": "SERVER",
            "display": "Number of Washers",
            "default": 4
        },

        {   "name": "RUNTIME",
            "display": "Running Time",
            "default": 1000
        }
    ]
}

graphs = [
    {   "name": "Queue vs Time",
        "x-axis": "TIME",
        "x-display": "Time (seconds)",
        "y-axis": "QUEUE",
        "y-display": "Number in Queue"
    },

    {   "name": "Server vs Time",
        "x-axis": "TIME",
        "x-display": "Time (seconds)",
        "y-axis": "SERVER",
        "y-display": "Servers Available"
    }
]

server = {
    "hostname": "localhost",
    "port": 9000
}
