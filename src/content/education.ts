export interface EducationEntry {
  institution: string;
  program: string;
  programNote?: string;
  years: string;
}

export const EDUCATION: EducationEntry[] = [
  {
    institution: "Kellogg School of Management, Northwestern University",
    program: "Executive Program, Organizational Leadership & AI Strategies",
    programNote:
      'LinkedIn lists this as "Executive Program in Organizational Leadership"; the resume lists "AI Strategies." Shown combined — see CONTENT_REVIEW.md.',
    years: "",
  },
  {
    institution: "Manipal Institute of Technology",
    program: "B.E., Mechanical Engineering",
    years: "2008 – 2012",
  },
  {
    institution: "Symbiosis Centre for Management & HR Development (SCMHRD)",
    program: "MBA, Marketing",
    years: "2014 – 2016",
  },
  {
    institution: "University of Michigan",
    program: "Programming for Everybody (Getting Started with Python)",
    years: "",
  },
];

export const CAREER_ARC = [
  "Mechanical Engineering",
  "Sales",
  "Marketing / MBA",
  "Product",
  "AI / Data",
  "Building",
];
