import React from 'react'

type Option = {
  value: string|number;
  label:string;
}
interface SelectOptionProps  {
  label:string;
  name:string;
  value: string|number;
  options: Option[];
  onChange: (name:string, value:number) => void;
}
function SelectOption({label,name,value,options,onChange}:SelectOptionProps) {
  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
  const newValue = parseInt(event.target.value, 10) || event.target.value;
   // Convert to number if it's a numeric field
 onChange(name, newValue);
};
  return (
    <>
      <label htmlFor={name} className="form-label">
        {label}
      </label>
      <select
        className='form-select'
        id={name}
        name={name}
        value={value}
        onChange={handleChange}
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>

    </>
  )
}
export default SelectOption;