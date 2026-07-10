export default function HomePage() {
  return (
    <div className="flex flex-col items-center p-24 gap-y-12">
      <div className="flex gap-4">
        <h1 className="text-5xl font-bold">Welcome to the</h1>
        <h1 className="text-5xl font-bold text-primary">APB Trainer</h1>
      </div>
      <h2 className="text-lg">Select 'learn' to begin learning algorithms or 'practice' to train.</h2>
    </div>
  );
}