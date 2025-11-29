//define a function that returns a promise that resolves after a delay

//the wait function combines Promise + siteTimeout to create an async delay
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

//this is mock function that simulates API calls with network delays and random failure 
async function mock(url) {
    console.log('Fetching data from', url);

    //network delay it makes it wait 0.5 seconds
    //this means the async function pause execution using await
    await wait(500); // Simulate network delay
    
    //Chance of failure
    //generate random number between 0 and 1 for success or failure
    const randomHappen = Math.random();//returns floating number

    //if random number is less than 0.7 or 70% simulates a network failure
    if (randomHappen <0.7){
        throw new Error ('Network Error Occurred');

    }
    else { //if succes THIS RETURNA A MOCK RESPONSE OBJECT
        return{
            status: 200,//http status code for ok
            data: {
                message: 'Data fetched successfully from ' }
            };
        }
    }
 //The main solution i though
    async function fetchDatawithRetry(url,maxRetries){
        for(let i = 0; i<maxRetries; i++){
            try{
                const result = await mock(url);
                return result;//success return 
            }
            catch (error){
                //if it failed catch an error here
                console.log(`Attempt ${i + 1} failed: ${error.message}`)

        //this will check if i have attempts left

        if(i<maxRetries -1){
            console.log('Retrying...');

            //her e is where the wait function is used
            await wait (1000); //wait 1 second before retrying
        }
        else {
            throw new Error('All retry attempts failed.');
        }
    }
}   

}

//async wrapper to use wair
//this is the main block that runs when the script loads
(async () => {
    console.log("starting task test");

    try{
        //attempting to fetch data from the given url 
        //which is maximum 5 retry attempting
        const data = await fetchDatawithRetry('https://api.eaglepoint.yoseph.com/data', 5);
        console.log('"\n final Value reult:', data);  

    }catch(finalError){
        //if all retries falls this catches the final error and log
        console.log("\n final Error:", finalError.message); 
    }
    })();

