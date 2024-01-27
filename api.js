const axios = require('axios');

async function fetchData() {
  const options = {
    method: 'GET',
    url: 'https://us-real-estate.p.rapidapi.com/v2/for-rent-by-zipcode',
    params: {
      zipcode: '48278',
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
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

// Call the async function
fetchData();