import { useEffect, useState } from 'react';
import './App.css';
import Table from "./components/Table";
import Form from "./components/Form";
import Footer from "./components/Footer";
import { TableRow, Filter, ConvertedRow } from "./types/types";


function App() {
  const headers = ["Name", "Locations", "Time", "Seasons", "Weather"];
  const API_URL = import.meta.env.URL;

  const [fishInfo, setFishInfo] = useState<TableRow[] | null>(null);
  const [filteredRows, setFilteredRows] = useState<ConvertedRow[] | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [filter, setFilter] = useState<Filter>({
    name: '',
    startTime: 6,
    endTime: 26,
    location: '',
    weather: 'Any',
    season: 'Any'
  });


  useEffect(() => {
    const transformDataToTableRows = (data: Record<string, any>): TableRow[] => {
      return Object.entries(data).map(([name, details]) => ({
        name,
        locations: details.locations,  // Already an array
        seasons: details.seasons,      // Already an array
        time: details.time,            // Already in number[][] format
        weather: details.weather       // Already an array
      }));
    };
    async function fetchFish() {
      try {
        const result = await fetch(API_URL);
        if (!result.ok) {
          throw new Error(`HTTP error! Status: ${result.status}`);
        }
        const data: TableRow[] = await result.json();
        console.log(data);
        const convertedData = transformDataToTableRows(data);
        setFishInfo(convertedData);
        ConvertRows()
      } catch (err) {
        setError((err as Error).message);
      } finally {
        setLoading(false);
      }
    };
    fetchFish();
  }, []);

  /** ✅ Convert fish data once it is available **/
  useEffect(() => {
    if (fishInfo) {
      ConvertRows();
    }
  }, [fishInfo]);

  /** ✅ Handle filter change **/
  const handleFilterChange = (name: string, value: string | number) => {
    setFilter(prevFilter => ({
      ...prevFilter,
      [name]: value,
    }));
  };

  /** ✅ Convert filtered rows **/
  const ConvertRows = () => {
    if (!fishInfo || !Array.isArray(fishInfo)) return;

    const filteredData: TableRow[] = getFilteredData();
    let convertedRows: ConvertedRow[] = filteredData.map(filteredRow => ({
      name: filteredRow.name,
      locations: filteredRow.locations.join(", "),
      time: filteredRow.time
        .map(([startTime, endTime]) => {
          if (endTime === 26) endTime = 2;
          const startTimeSuffix = startTime > 12 ? "pm" : "am";
          const endTimeSuffix = endTime > 12 ? "pm" : "am";
          return `${startTime % 12 || 12}${startTimeSuffix} to ${endTime % 12 || 12}${endTimeSuffix}`;
        })
        .join(", "),
      seasons: filteredRow.seasons.join(", "),
      weather: filteredRow.weather.join(", ")
    }));
    setFilteredRows(convertedRows);
    console.log(convertedRows.length);
  };

  /** ✅ Filtering logic **/
  const getFilteredData = () => {
    if (!fishInfo || !Array.isArray(fishInfo)) return [];
    console.log(fishInfo.length);
    return fishInfo.filter(item => {
      // Name Match
      console.log(item.name);
      const nameMatch = item.name?.includes(filter.name) || filter.name === '';

      // Time Match (overlap check)
      const timeMatch = item.time.some(([start, end]) => {
        return (
          (filter.startTime <= start && end<=filter.endTime ) // Check for overlap
        );
      });

      // Location Match
      const locationMatch = item.locations?.includes(filter.location) || filter.location === '';

      // Season Match
      const seasonMatch = item.seasons?.includes(filter.season) || filter.season === 'Any';

      // Weather Match
      const weatherMatch = item.weather?.includes(filter.weather) || filter.weather === 'Any';
      console.log(nameMatch,timeMatch,locationMatch,seasonMatch);
      return nameMatch && timeMatch && locationMatch && seasonMatch && weatherMatch;
    });
  };


  return (
    <>
      <h1>Stardew Valley Fish</h1>
      {error && <p>Error: {error}</p>}
      <section>
        <article>
          {!loading && <Form onFilterChange={handleFilterChange} filter={filter} onFilter={ConvertRows} />}
        </article>
        <article>
          {!loading && Array.isArray(filteredRows) && <Table headers={headers} rows={filteredRows}  />}
        </article>
      </section>
      <footer>
        <Footer />
      </footer>
    </>
  );
}

export default App;
