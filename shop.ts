import axios from 'axios';
import { getSthUrl } from './endpoints';


export async function getSth(): Promise<number>{
    let response = await axios.get(getSthUrl)
    return response.data

}