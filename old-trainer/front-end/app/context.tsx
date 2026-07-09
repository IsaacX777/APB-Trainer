import { createContext, useContext, useState, ReactNode } from 'react';

const defaultCases: Map<string, Map<string, number[]>> = new Map([
  ['lxs', new Map([
    ['UFR', Array.from({ length: 30 }, (_, i) => i)],
    ['RFU', Array.from({ length: 30 }, (_, i) => i)],
    ['FUR', Array.from({ length: 30 }, (_, i) => i)],
    ['DFR', Array.from({ length: 8 }, (_, i) => i)],
    ['RDF', Array.from({ length: 9 }, (_, i) => i)],
    ['FRD', Array.from({ length: 9 }, (_, i) => i)]
  ])],
  ['eo_pair', new Map([
    ['dBR', Array.from({ length: 11 }, (_, i) => i)],
    ['dFR', Array.from({ length: 11 }, (_, i) => i)],
    ['OU', Array.from({ length: 31 }, (_, i) => i)],
    ['OR', Array.from({ length: 31 }, (_, i) => i)],
    ['MU', Array.from({ length: 32 }, (_, i) => i)],
    ['MR', Array.from({ length: 32 }, (_, i) => i)]
  ])]
]);

interface AppContextType {
  selection: string;
  setSelection: (selection: string) => void;
  cases: Map<string, Map<string, number[]>>;
  setCases: (cases: Map<string, Map<string, number[]>>) => void;
}

const AppContext = createContext<AppContextType>({
  selection: 'lxs',
  setSelection: () => {},
  cases: defaultCases,
  setCases: () => {}
});

export const AppProvider = ({ children }: { children: ReactNode }) => {
  const [selection, setSelection] = useState<string>('lxs');
  const [cases, setCases] = useState<Map<string, Map<string, number[]>>>(defaultCases);

  return (
    <AppContext.Provider value={{ selection, setSelection, cases, setCases }}>
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => useContext(AppContext);
