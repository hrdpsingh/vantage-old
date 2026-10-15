import { CommitActivity } from "./Sections/CommitActivity";
import { useLocation } from "react-router-dom";
import { Contributors } from "./Sections/Contributors";
import { PunchCard } from "./Sections/PunchCard";
import { Overview } from "./Sections/Overview";
import { Languages } from "./Sections/Languages";

export function Dashboard() {
  const location = useLocation();
  const username = location.state?.username;
  const repository = location.state?.repository;

  return (
    <main className="p-4 bg-blue-100 min-h-screen gap-8">
      <Overview username={username} repository={repository}></Overview>
      <CommitActivity
        username={username}
        repository={repository}
      ></CommitActivity>
      <Contributors username={username} repository={repository}></Contributors>
      <PunchCard username={username} repository={repository}></PunchCard>
      <Languages username={username} repository={repository}></Languages>
    </main>
  );
}
