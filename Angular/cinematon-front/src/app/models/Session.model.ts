import { Time } from "@angular/common";

export interface Session{
    session_id: number,
    start_time: string,
    end_time: string,
    film: number,
    hall: number,
    cost: number
}