import { withPageAuthRequired, getSession } from "@auth0/nextjs-auth0";

export default function Home({ user }: any) {
  return (
    <div>
      <h1>Geriatric B2B MVP</h1>
      <p>Welcome {user?.name}</p>
    </div>
  );
}

export const getServerSideProps = withPageAuthRequired();
