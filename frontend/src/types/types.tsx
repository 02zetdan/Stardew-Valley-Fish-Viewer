 export type TableRow = {
    name: string;
    locations: string[];
    time: number[][];
    seasons: string[];
    weather: string[];
  }
  export type ConvertedRow = {
    name:string;
    locations:string;
    time:string;
    seasons:string;
    weather:string;
  }
  export type Filter = {
    name: string;
    startTime: number;
    endTime: number;
    location: string;
    weather: string;
    season: string;

  }
