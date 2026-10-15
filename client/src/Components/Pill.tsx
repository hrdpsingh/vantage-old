import type { ReactNode } from "react";

interface PillProps {
  children: ReactNode;
}

export function Pill({ children }: PillProps) {
  return (
    <div className="bg-blue-300 border border-blue-600 p-4 rounded-full">
      {children}
    </div>
  );
}
