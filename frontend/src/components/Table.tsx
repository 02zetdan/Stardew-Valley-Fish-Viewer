
import { ConvertedRow} from "../types/types";

interface TableProps {
  headers: string[];
  rows: ConvertedRow[];

}
export const Table = ({headers,rows,onFilter}:TableProps) => {
  return (
    <>
    <div className="container mt-4">
    <table className="table table-hover table-bordered border border-sucess" >
      <thead>
        <tr>
        {headers.map((header) => (
            <th key={header}>{header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((columns,index) =>(
          <tr key={index}>
          <td>{columns.name}</td>
          <td>{columns.locations}</td>
          <td>{columns.time}</td>
          <td>{columns.seasons}</td>
          <td>{columns.weather}</td>
          </tr>
        ))}
      </tbody>
    </table>
    </div>
    </>
  )
}
export default Table;