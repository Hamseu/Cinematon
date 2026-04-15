import { Time } from "@angular/common";

export interface Session{
    id: number,
    start_time: string,
    end_time: string,
    film_id: number,
    hall_id: number,
    cost: number
}