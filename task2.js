//the wait function combines Promise + siteTimeout
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
async function mock(url) {
    console.log('Fetching data from', url);

    //network delay it makes it wait 0.5 seconds
    await wait(500); // Simulate network delay
    
    //Chance of failure
    const randomHappen = Math.random();

    if (randomHappen <0.7){
        throw new Error ('Network Error Occurred');

    }
    else {
        return{
            status: 200,
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

//async wrapper to run the code

(async () => {
    console.log("starting task test");

    try{
        const data = await fetchDatawithRetry('https://api.eaglepoint.yoseph.com/data', 5);
        console.log('"\n final Value reult:', data);  

    }catch(finalError){
        console.log("\n final Error:", finalError.message); 
    }
    })();

