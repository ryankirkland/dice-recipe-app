export default function ProgressBar({ progress }) {
    return (
      <div className="w-full bg-gray-300 rounded-full h-3 mt-4">
        <div
          className="bg-green-500 h-3 rounded-full transition-all duration-500 ease-out"
          style={{ width: `${progress}%` }}
        ></div>
      </div>
    );
  }
  