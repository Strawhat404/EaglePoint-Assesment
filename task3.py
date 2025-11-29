from typing import Dict,List
import time #to work with time stamps and measure time
"""
the following class implements a sliding window rate limiter that 
tracks API reqquest"""
class RateLimiter:
    #CONSTRUCTOR

    #Initializes the rate limiter configurable limits
    def __init__(self,limit: int=5,window_seconds: int=60):#runs automatatically when a new Ratelimiter is created
        
        
      #Rate limit configuration
        self.limit = limit 
        #maximum number of requests allowed per time unit

        #the time duration in seconds
        self.window = window_seconds 

        #serve as user request history storage
        self.user_requests : Dict[str,List[float]] = {} #stores user request timestamps}


    """this is the core method that decides or chenks to allow or block reques
    -It implements the sliding window algorithm to track requests per user
    -under rate limit: Request is allowed over late limit: request is blocked"""
    
    def request_allowance(self, user_id:str) -> bool:
        # Get current time
        current_time = time.time()

        timestamps = self.user_requests.get(user_id, [])

        valid_timestamps = [t for t in timestamps if (current_time - t) < self.window]
        
        # Initialize user if they don't exist
        #check if it's the first request from this user creatE an empty list for it
        if user_id not in self.user_requests:
            self.user_requests[user_id] = [] #initializez with empty history
        
        #get list of previous timestamps for this user
        timestamps = self.user_requests[user_id]
        
       #filter out timestamps outside the current sliding window
       #and keeps requests only that occured within the time window
        valid_timestamps = [t for t in timestamps if (current_time - t) < self.window]
        
        # if user is under the rate limit it allow the request
        if len(valid_timestamps) < self.limit:

           #add the current quest time stamp to the valid timestamps
            valid_timestamps.append(current_time)
            self.user_requests[user_id] = valid_timestamps
            return True #signals that request is allowed
        else:
            self.user_requests[user_id] = valid_timestamps
            # BLOCKs it, Do not add new timestamp
            return False #signals that request is blocked

#this provides working examples and tests for the rate limiter  functionality
if __name__ == "__main__":
    #create rate limiter instance with 5 requests per 60 seconds
    limiter = RateLimiter(limit=5, window_seconds=60)
    user = "test_user1"

    print(f"Testing Rate Limiter  ({limiter.limit} requests per {limiter.window}s)")

    # Test Scenario: first 6 requests from the same user
    #since it is under 5 request it has to be allowed
    for i in range(1, 7):
        is_allowed = limiter.request_allowance(user)
        status = " Allowed" if is_allowed else "you are  Blocked"
        print(f"Request {i}: {status}")