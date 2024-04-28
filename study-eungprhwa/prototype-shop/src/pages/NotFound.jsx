import { useNavigate } from "react-router";

function NotFound() {
  const navigate = useNavigate();
  return (
    <div className="container">
      <main>
        <div className="notfound">
          <h1>Not Found</h1>
          <p>You have requested a page that does not exist.</p>
          <button
            className="btn btn--secondary"
            style={{ width: "100%", marginTop: 10 }}
            onClick={() => {
              navigate("/", {
                replace: true,
              });
            }}
          >
            Go to Main Page
          </button>
        </div>
      </main>
    </div>
  );
}

export default NotFound;
