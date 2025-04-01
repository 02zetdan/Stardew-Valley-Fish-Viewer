import React from 'react'
import { useState } from 'react';
interface SearchOptionProps {
  text:string;
  label:string;
  placeholder?:string;
  name:string;
  onChange: (name:string,text:string) => void;
}
function SearchOption({text,label,placeholder,name,onChange}:SearchOptionProps)  {

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    onChange(name, event.target.value);
  };
  return (
    <>
    <label htmlFor={name} className="form-label">
      {label}
    </label>
    <input
      className='form-control'
      type="text"
      id={name}
      name={name}
      value={text}
      placeholder={placeholder}
      onChange={handleChange}
    />
    </>
  );
}
export default SearchOption;