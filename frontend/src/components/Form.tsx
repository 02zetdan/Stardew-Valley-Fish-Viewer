import SearchOption from "./SearchOption";
import SelectOption from "./SelectOption";
import Button from "./Button";

type Filter = {
  name: string;
  startTime: number;
  endTime: number;
  location: string;
  weather: string;
  season: string;
};

interface FormProps {
  filter: Filter;
  onFilterChange: (name: string, value: string | number) => void;
  onFilter: () => void;
}

function Form({ onFilterChange, onFilter, filter }: FormProps) {
  const startTimeOptions = [
    { value: 6, label: '6am' },
    { value: 9, label: '9am' },
    { value: 12, label: '12pm' },
    { value: 15, label: '3pm' },
  ];

  const endTimeOptions = [
    { value: 26, label: '2am' },
    { value: 12, label: '12pm' },
    { value: 15, label: '3pm' },
    { value: 18, label: '6pm' },
    { value: 21, label: '9pm' },
  ];

  // Weather options
  const weatherOptions = [
    { value: 'Any', label: 'Any weather' },
    { value: 'Sun', label: 'Sun' },
    { value: 'Wind', label: 'Wind' },
    { value: 'Rain', label: 'Rain' },
  ];

  // Season options
  const seasonOptions = [
    { value: 'Any', label: 'Any season' },
    { value: 'Spring', label: 'Spring' },
    { value: 'Summer', label: 'Summer' },
    { value: 'Fall', label: 'Fall' },
    { value: 'Winter', label: 'Winter' },
  ];

  const handleReset = () => {
    onFilterChange('name', '');
    onFilterChange('startTime', 6);
    onFilterChange('endTime', 26);
    onFilterChange('location', '');
    onFilterChange('weather', 'Any');
    onFilterChange('season', 'Any');
    onFilter();
  };

  return (
    <form className="bg-light p-4 rounded shadow-lg" style={{ maxWidth: '600px', margin: 'auto' }}>
      <h2 className="text-center mb-4 text-uppercase" style={{ fontFamily: 'Press Start 2P', fontSize: '24px' }}>Fish Table</h2>

      <div className="row">
        <div className="col-12 col-md-6 mb-3">
          <SelectOption
            label="Start Time"
            name="startTime"
            value={filter.startTime}
            options={startTimeOptions}
            onChange={onFilterChange}
          />
        </div>

        <div className="col-12 col-md-6 mb-3">
          <SelectOption
            label="End Time"
            name="endTime"
            value={filter.endTime}
            options={endTimeOptions}
            onChange={onFilterChange}
          />
        </div>

        <div className="col-12 col-md-6 mb-3">
          <SelectOption
            label="Season"
            name="season"
            value={filter.season}
            options={seasonOptions}
            onChange={onFilterChange}
          />
        </div>

        <div className="col-12 col-md-6 mb-3">
          <SelectOption
            label="Weather"
            name="weather"
            value={filter.weather}
            options={weatherOptions}
            onChange={onFilterChange}
          />
        </div>

        <div className="col-12 mb-3">
          <SearchOption
            text={filter.name}
            label="Search by Name"
            placeholder="Pufferfish"
            name="name"
            onChange={onFilterChange}
          />
        </div>

        <div className="col-12 mb-3">
          <SearchOption
            text={filter.location}
            label="Location"
            placeholder="River"
            name="location"
            onChange={onFilterChange}
          />
        </div>
      </div>

      <div className="d-flex justify-content-end">
        <div className="btn-group" role="group">
          <Button onClick={handleReset} className="btn-outline-secondary px-4 py-2 me-3">
            Reset Filters
          </Button>
          <Button onClick={onFilter} className="btn-outline-primary px-4 py-2">
            Filter
          </Button>
        </div>
      </div>
    </form>
  );
}

export default Form;
