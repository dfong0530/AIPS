import React from "react";
function Button(props) {
    return (
        <button className="font-bold text-sm text-gray-light px-4 py-1 mx-5 hover:bg-gray-bg rounded-full transition duration-300 ease-in-out w-20 overflow-hidden whitespace-nowrap">
            {props.children}
        </button>
    );
  }
export default function InstructionBar() {
    return (
        <div className="flex justify-center mt-6">
            <nav className="inline-flex justify-center items-center bg-gray-default rounded-full">
                <Button>Support</Button>
                <div className="font-bold text-xl text-red-default px-4 py-2 select-none">AIPS</div>
                <Button>Login</Button>
            </nav>
        </div>
    );
}
