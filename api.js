// const axios = require('axios');

// async function fetchData() {
//   const options = {
//     method: 'GET',
//     url: 'https://us-real-estate.p.rapidapi.com/v2/for-rent-by-zipcode',
//     params: {
//       zipcode: '48104',
//       limit: '10',
//       offset: '0',
//       sort: 'lowest_price'
//     },
//     headers: {
//       'X-RapidAPI-Key': 'bcaeda5567mshf61ffc86fd30d06p107858jsn1b73ed124fbd',
//       'X-RapidAPI-Host': 'us-real-estate.p.rapidapi.com'
//     }
//   };

//   try {
//     const response = await axios.request(options);
//     console.log(response.data);
//   } catch (error) {
//     console.error(error);
//   }
// }

// // Call the async function
// fetchData();


const axios = require('axios');
const fs = require('fs');

async function fetchDataAndSaveToFile() {
  const options = {
    method: 'GET',
    url: 'https://us-real-estate.p.rapidapi.com/v2/for-rent-by-zipcode',
    params: {
      zipcode: '48104',
      limit: '10',
      offset: '0',
      sort: 'lowest_price'
    },
    headers: {
      'X-RapidAPI-Key': 'bcaeda5567mshf61ffc86fd30d06p107858jsn1b73ed124fbd',
      'X-RapidAPI-Host': 'us-real-estate.p.rapidapi.com'
    }
  };

  try {
    const response = await axios.request(options);

    // Save the response data to a file
    fs.writeFileSync('apiResponse.json', JSON.stringify(response.data, null, 2));

    console.log('Data saved to apiResponse.json');
  } catch (error) {
    console.error(error);
  }
}

// Call the async function
fetchDataAndSaveToFile();