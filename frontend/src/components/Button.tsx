import { ReactNode } from "react";

interface ButtonProps {
    children: ReactNode
    onClick: () => void;

}
function Button({children,onClick}:ButtonProps){
    return (
        <>
        <button type="button" className="btn btn-primary" onClick={onClick} >{children}</button>
        </>
    );
}
export default Button;