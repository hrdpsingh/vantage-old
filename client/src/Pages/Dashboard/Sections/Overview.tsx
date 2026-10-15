import { Card } from "../../../Components/Card";
import { Info } from "../../../Components/Info";
import { useFetch } from "../../../hooks/useFetch";
import ClipLoader from "react-spinners/ClipLoader";
import type { Details } from "../../../types/repository";
import { Pill } from "../../../Components/Pill";

interface Data {
  star_count: number;
  fork_count: number;
  issues: number;
  last_update: string;
  topics: string[];
}

export function Overview({ username, repository }: Details) {
  const url = `http://127.0.0.1:8000/repository/${username}/${repository}/overview`;
  const data = useFetch<Data>(username, repository, url);

  return (
    <div>
      {data ? (
        <div>
          <div className="flex flex-col sm:flex-row gap-4">
            <Card>
              <Info header="Stars" value={String(data.star_count)} />
            </Card>
            <Card>
              <Info header="Forks" value={String(data.fork_count)} />
            </Card>
            <Card>
              <Info header="Issues" value={String(data.issues)} />
            </Card>
            <Card>
              <Info header="Last Update" value={data.last_update} />
            </Card>
          </div>
          <div className="flex flex-row flex-wrap items-center gap-2">
            {data.topics.map((topic, index) => (
              <Pill key={index}>
                <p>{topic}</p>
              </Pill>
            ))}
          </div>
        </div>
      ) : (
        <ClipLoader></ClipLoader>
      )}
    </div>
  );
}
