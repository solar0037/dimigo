import { useNavigate } from "react-router";

export default function WrongRequest() {
  const navigate = useNavigate();
  return (
    <main>
      <div className="wrongrequest">
        <h1>Wrong Request</h1>
        <p>
          You have sent an invalid request. You may have entered this checkout
          page without selecting any items.
        </p>
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
  );
}
