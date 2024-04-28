import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Checkout from "./pages/Checkout";
import NotFound from "./pages/NotFound";
import AppStateProvider from "./Providers/AppStateProvider";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          exact
          element={
            <AppStateProvider>
              <Home />
            </AppStateProvider>
          }
        />
        <Route
          path="/checkout"
          exact
          element={
            <AppStateProvider>
              <Checkout />
            </AppStateProvider>
          }
        />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
