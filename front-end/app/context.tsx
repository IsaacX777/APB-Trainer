import { createContext, useContext, useState, ReactNode } from 'react';

const defaultCases: Map<string, Map<string, number[]>> = new Map([
  ['lxs', new Map([
    ['UFR', Array.from({ length: 30 }, (_, i) => i)],
    ['RFU', []]
  ])],
  ['eo_pair', new Map([
    ['dBR', [1]]
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
