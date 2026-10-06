def validate_input(data: dict) -> bool:
    """Validates roblox automation payload structure."""
    required_fields = {"user_id": int, "action": str, "params": dict}
    
    try:
        for field, expected_type in required_fields.items():
            if field not in data:
                return False
            if not isinstance(data[field], expected_type):
                return False
        
        # Ensure parameters aren't excessive for API limits
        if len(data.get("params", {})) > 50:
            return False
            
        return True
    except (TypeError, ValueError):
        return False

def process_main_loop(queue):
    """Main processing loop with input validation."""
    while True:
        task = queue.get()
        if not task:
            continue
            
        if not validate_input(task):
            print(f"Discarding invalid task: {task}")
            continue
            
        try:
            # Simulate automation execution logic
            print(f"Executing action {task['action']} for {task['user_id']}")
        except Exception as e:
            print(f"Processing error: {e}")