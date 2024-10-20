export * from './models';

import axios from 'axios';

async function searchTikTokVideos(keywords: string, count: string = '30', cursor: string = '0') {
    const options = {
        method: 'GET',
        url: 'https://tiktok-api15.p.rapidapi.com/index/Tiktok/searchVideoListByKeywords',
        params: { keywords, count, cursor },
        headers: {
            'x-rapidapi-key': '36d89111a2msh4ba98e6cc64bc41p1b0c41jsn27ddea8cadd7',
            'x-rapidapi-host': 'tiktok-api15.p.rapidapi.com'
        }
    };

    try {
        const response = await axios.request(options);
        return response.data;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

