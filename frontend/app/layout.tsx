import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Gipsy Chat",
  description: "AI Chat with Notion Integration",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
