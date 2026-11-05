import logging

logger = logging.getLogger(__name__)

def validate_input(data: dict) -> bool:
    """Validates roblox automation payload structure."""
    required_keys = ['script_id', 'execution_delay', 'server_id']
    if not all(key in data for key in required_keys):
        return False
    if not isinstance(data.get('execution_delay'), (int, float)):
        return False
    return True

def run_processing_loop(task_queue):
    """Main loop for processing automation tasks."""
    logger.info("Starting roblox automation processor")
    
    while True:
        task = task_queue.get()
        if task is None:
            break
            
        if not validate_input(task):
            logger.warning(f"Invalid task payload skipped: {task}")
            continue
            
        try:
            execute_task(task)
        except Exception as e:
            logger.error(f"Task execution failed: {e}")
        
        task_queue.task_done()

def execute_task(task):
    """Handles actual roblox injection logic."""
    logger.info(f"Executing task: {task['script_id']}")

if __name__ == "__main__":
    # Example usage
    from queue import Queue
    q = Queue()
    q.put({'script_id': 'rbx_script_01', 'execution_delay': 0.5, 'server_id': 12345})
    q.put(None)
    run_processing_loop(q)