# Edify AI (Gen-ed)

_Revolutionizing Education with AI-Powered Courses, Immersive Meetings, and Powerful Career Tools_

<!-- 3D Bot Animation -->
<p align="center">
  <img src="https://media1.tenor.com/m/LCccd3UmffEAAAAd/clydeai-discord.gif" alt="Edify AI 3D Bot" width="250">
</p>

<p align="center">
  <a href="#-key-features">Features</a> •
  <a href="#-why-edify-ai">Why Edify AI</a> •
  <a href="#-who-is-this-for">Who Is This For</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-developer--contributor-guide">Developer Guide</a>
</p>

---

## 🎯 Latest Updates (2024)

### 🚀 Major Features Added

- **Multi-Agent Resume ATS Analysis System**: Production-ready LangGraph-based multi-agent system deployed on Google Cloud Run
- **Interactive Dashboard**: Comprehensive visualization dashboard with charts, detailed breakdowns, and actionable insights
- **Cloud Deployment**: Backend API fully deployed and production-ready on Google Cloud Run
- **Structured Data Extraction**: Advanced AI-powered resume parsing with Pydantic validation
- **Parallel Agent Execution**: Five specialized agents working simultaneously for faster analysis

### 🏗️ Architecture Improvements

- **LangGraph Orchestration**: Sophisticated workflow management for multi-agent coordination
- **Vertex AI Integration**: Direct integration with Google's Gemini 2.0 Flash model
- **Type-Safe APIs**: End-to-end TypeScript/Python type safety
- **Production Infrastructure**: Docker containerization, Cloud Run deployment, CI/CD pipeline

---

## ✨ Overview

**Edify AI** was born from a stark reality: **5 out of 6 students** are frustrated with traditional, outdated university education. With static curricula and limited access to enriching events, hackathons, and networking, today's learners need a new approach. 

Edify AI delivers a **personalized, dynamic learning platform** that adapts to industry demands and connects a global community of forward-thinking students. Whether you're preparing for your dream job, building new skills, or seeking mentorship, Edify AI provides everything you need in one powerful platform.

---

## 🚀 Key Features

### 🎓 AI-Powered Personalized Learning

**Learn at Your Own Pace, Your Way**

- **Instant Course Creation**
  - Tell us what you want to learn, and AI creates a complete course in seconds
  - Automatically finds and curates the best educational videos with **85% relevancy**
  - No more spending hours searching for quality content

- **Personalized Learning Paths**
  - Structured pathways from complete beginner to industry expert
  - AI adapts to your learning style, pace, and goals
  - Track your progress with detailed analytics and insights
  - **Boosts learning efficiency by up to 90%** compared to traditional methods

- **Interactive Learning Experience**
  - Built-in code editor for hands-on programming practice
  - Video-based lessons with curated multimedia content
  - Community forums for each course to ask questions and share insights
  - Learning streaks and achievements to keep you motivated

**How It Helps You**: Stop wasting time on irrelevant content. Get a customized learning plan that matches your career goals and learning style, complete with the best resources handpicked for you.

---

### 🤖 AI Agent Meetings - Your Personal Tutor & Interview Coach

**Practice, Learn, and Improve Anytime**

- **Mock Interview Sessions**
  - Practice with AI-generated questions tailored to your target job
  - Real-time speech-to-text transcription captures everything you say
  - Get instant feedback on your answers, tone, and delivery
  - Review detailed analytics showing areas for improvement
  - **Boost interview success rates by up to 70%**

- **Personalized Tutoring**
  - One-on-one sessions with AI tutors available 24/7
  - Get help with any subject or topic at any time
  - Practice conversations, presentations, and role-playing scenarios
  - Automatic recording so you can review sessions later

- **Career Coaching**
  - Practice salary negotiations
  - Improve public speaking skills
  - Work on communication and presentation abilities
  - Build confidence through repeated practice

**How It Helps You**: No more expensive coaching or waiting for availability. Get instant, personalized practice sessions that adapt to your needs, helping you build skills and confidence faster.

---

### 💼 Career Readiness Tools

**Land Your Dream Job with Confidence**

- **Multi-Agent Resume ATS Analysis System** 🆕
  - **Advanced LangGraph Multi-Agent Architecture**: Five specialized AI agents working in parallel to analyze your resume
  - **Comprehensive Section Scoring**: 
    - Skills matching (35% weight)
    - Work experience relevance (35% weight)
    - Education alignment (15% weight)
    - Projects portfolio (10% weight)
    - Meta information (5% weight - seniority, domains, languages)
  - **Structured Resume Extraction**: AI-powered parsing that extracts contact info, skills, experience, education, projects, and metadata
  - **Interactive Dashboard**: 
    - Real-time visualizations with bar charts, pie charts, and radar charts
    - Detailed breakdowns for each section with progress indicators
    - Side-by-side resume and job description comparison
    - Actionable recommendations with missing requirements highlighted
    - Historical analysis tracking to monitor improvements over time
  - **Weighted Score Aggregation**: Intelligent algorithm that combines all section scores for accurate overall matching
  - **Production-Ready Backend**: Deployed on Google Cloud Run with Vertex AI integration
  - **Export & Share**: Download comprehensive PDF reports of your analysis

- **Smart Mock Interview Platform**
  - Upload your resume and job description
  - AI generates realistic interview questions specific to the role
  - Practice with video recording and live transcription
  - Receive detailed feedback with ratings (1-10) and actionable improvement tips
  - Compare your answers with model responses
  - Track progress across multiple interviews

- **ATS-Optimized Resume Builder**
  - Create resumes that pass Applicant Tracking Systems
  - AI-powered content suggestions based on job descriptions
  - Multiple professional templates
  - Export to PDF with perfect formatting
  - Tips for making your resume stand out

- **Performance Analytics**
  - See your interview performance trends over time
  - Identify strengths and areas needing improvement
  - Set goals and track your progress toward career readiness

**How It Helps You**: Eliminate interview anxiety and job search stress. Get comprehensive, multi-dimensional resume analysis powered by cutting-edge AI agents. Practice until you're confident, get personalized feedback, and create resumes that actually get noticed by employers.

---

### 🤖 Multi-Agent Resume Analysis System (Technical Deep Dive)

**Architecture:**
- **LangGraph Orchestrator**: Manages the entire workflow from resume extraction to score aggregation
- **Resume Extractor Agent**: Uses Vertex AI structured output to parse resumes into structured JSON
- **Five Scoring Agents** (executed in parallel):
  1. **Skills Agent** (35% weight): Matches technical and soft skills against job requirements
  2. **Experience Agent** (35% weight): Evaluates work experience relevance and depth
  3. **Education Agent** (15% weight): Assesses educational background alignment
  4. **Projects Agent** (10% weight): Analyzes portfolio and project relevance
  5. **Meta Agent** (5% weight): Evaluates seniority level, domain expertise, and language proficiency
- **Score Aggregator**: Combines all section scores using weighted averaging algorithm
- **HTTP API Server**: Lightweight Python server deployed on Cloud Run

**Technology Stack:**
- **Python 3.13** with LangGraph for agent orchestration
- **Vertex AI Gemini 2.0 Flash** for AI inference
- **Pydantic** for data validation and structured outputs
- **Cloud Run** for serverless deployment
- **Docker** for containerization

**Performance:**
- **Sub-5 second** analysis time with parallel agent execution
- **Production-ready** with health checks and error handling
- **Scalable** architecture that handles concurrent requests

**Deployment:**
- ✅ **Deployed**: Backend API running on Google Cloud Run
- ✅ **Integrated**: Frontend connected to production backend
- ✅ **Monitored**: Health checks and logging in place

---

### 👥 Community & Networking

**Connect, Learn, and Grow Together**

- **Interactive Course Forums**
  - Ask questions, share insights, and help fellow learners
  - Course-specific discussion boards for focused conversations
  - Get answers from peers and mentors
  - Build your professional network while learning

- **Events Discovery**
  - Find hackathons, networking events, and workshops
  - Connect with opportunities that match your interests
  - Join a community of **500,000+ students** across **30+ countries**
  - Access exclusive opportunities and resources

- **Global Learning Community**
  - Learn from students worldwide
  - Share experiences and best practices
  - Collaborate on projects and challenges
  - Build lasting professional connections

**How It Helps You**: Never learn alone. Join a vibrant community of learners, get support when you're stuck, discover opportunities, and build a network that extends beyond the platform.

---

### 📊 Smart Progress Tracking

**Know Exactly Where You Stand**

- **Comprehensive Dashboard**
  - See all your courses, interviews, and learning paths in one place
  - Track learning streaks to maintain consistency
  - View completion rates and time invested
  - Set and achieve learning milestones

- **Detailed Analytics**
  - Understand your learning patterns
  - Identify your strongest and weakest areas
  - Get recommendations for what to focus on next
  - Celebrate achievements and stay motivated

**How It Helps You**: Stop guessing if you're making progress. Get clear insights into your learning journey, stay accountable, and make data-driven decisions about your education.

---

## 🌟 Why Edify AI?

### Your Unique Advantages

1. **AI Does the Heavy Lifting**
   - No more manual course creation or content curation
   - Get personalized learning plans instantly
   - Save **50% of your time** on finding quality resources

2. **Practice Makes Perfect**
   - Unlimited mock interviews whenever you need them
   - Get detailed feedback that actually helps you improve
   - Build confidence through repeated practice without judgment

3. **Everything in One Place**
   - Courses, interviews, resume building, and community
   - No need to juggle multiple tools and platforms
   - Streamlined experience saves time and reduces overwhelm

4. **Learn What Actually Matters**
   - Content curated for real-world relevance
   - Skills that employers actually want
   - Stay ahead of industry trends and demands

5. **Access Anytime, Anywhere**
   - 24/7 availability - learn and practice on your schedule
   - Work around your job, classes, or other commitments
   - No scheduling conflicts or waiting lists

6. **Affordable & Accessible**
   - Premium learning tools without premium prices
   - No expensive coaching or course fees
   - Democratizing access to quality education

---

## 👤 Who Is This For?

### Perfect For:

- **Students** seeking to supplement their university education with practical, industry-relevant skills
- **Job Seekers** preparing for interviews and building standout resumes
- **Career Changers** learning new skills and transitioning to different fields
- **Professionals** looking to upskill and stay competitive in their industry
- **Self-Learners** who prefer personalized, self-paced education
- **Anyone** frustrated with traditional, one-size-fits-all education

### Success Stories:

- **75%** of users report significant gains in industry-relevant skills
- **Up to 90%** improvement in learning efficiency
- **70%** boost in interview success rates
- **85%** of community members connect with vital opportunities

---

## 🎯 How It Helps Users

### For Job Seekers

**Problem**: Job interviews are stressful, and you never know what to expect.

**Solution**: Practice unlimited mock interviews with questions tailored to your specific job. Get detailed feedback on your answers, tone, and delivery. Build confidence through repeated practice until you're ready to ace the real thing.

**Result**: Walk into interviews feeling prepared and confident, knowing you've practiced and improved.

---

### For Skill Learners

**Problem**: You don't know where to start learning, and most courses are generic or outdated.

**Solution**: Tell AI what you want to learn, and get a complete, personalized course in seconds. Learn with curated content from the best sources, track your progress, and get support from a community of learners.

**Result**: Learn efficiently with a clear path forward, saving time and avoiding information overload.

---

### For Career Changers

**Problem**: You want to switch careers but don't know where to begin or what skills you need.

**Solution**: Get personalized learning paths that take you from beginner to job-ready. Practice interviews for your new field, build relevant skills, and create a resume that showcases your transition.

**Result**: Make a successful career change with confidence, knowing you have the skills and preparation needed.

---

### For Busy Professionals

**Problem**: You want to upskill but don't have time for traditional courses.

**Solution**: Learn at your own pace, on your schedule. Access courses and practice sessions 24/7. Get bite-sized, focused content that fits your busy lifestyle.

**Result**: Keep your skills current and competitive without disrupting your work or life.

---

## 📈 Impact & Results

### Real Outcomes

- **500,000+ students** served across **30+ countries**
- **75%** report significant skill improvements
- **85%** connect with opportunities through the platform
- **90%** improvement in learning efficiency
- **70%** boost in interview success rates
- **Production-Ready Multi-Agent System** deployed on Google Cloud Run
- **Sub-5 second** resume analysis response times with parallel agent execution

### What Users Are Saying

> "I aced my interview after practicing with Edify AI. The feedback was incredibly detailed and helped me improve areas I didn't even know needed work." - Recent Graduate

> "The personalized learning paths are a game-changer. I went from beginner to job-ready in half the time I expected." - Career Changer

> "Finally, a platform that actually helps me learn what matters for my career. The AI course generation saves me hours of research." - Working Professional

---

## 🛤️ What's Coming Next

We're constantly improving based on user feedback:

- **Enhanced Multi-Agent Systems**: Expanding the agent architecture to other features (course generation, interview feedback, etc.)
- **Real-Time Resume Optimization**: Live suggestions as you edit your resume
- **Advanced Analytics**: Deeper insights into your learning patterns and progress
- **Mobile App**: Learn and practice on the go
- **More Languages**: Expanding globally to serve more learners
- **AR/VR Integration**: Immersive learning experiences for hands-on practice
- **Career Matching**: AI-powered job matching based on your skills and interests
- **Vertex AI Agent Engine Integration**: Native deployment of agents to Vertex AI Agent Engine (currently using Cloud Run)

---

## ⚙️ Getting Started

### Quick Start

1. **Sign Up for Free**
   - Create your account in seconds
   - No credit card required
   - Start exploring immediately

2. **Choose Your Path**
   - Browse courses in your field of interest
   - Start your first mock interview
   - Build your first resume
   - Join a learning path

3. **Set Your Goals**
   - Define what you want to achieve
   - Get personalized recommendations
   - Start your learning journey

4. **Track Your Progress**
   - Monitor your improvement over time
   - Celebrate your achievements
   - Stay motivated with insights and analytics

### Access the Platform

- **Website**: [Your Website URL]
- **Support**: [Support Email/Channel]
- **Community**: Join our forums to connect with other learners
- **API Documentation**: See `docs/` folder for API endpoints and integration guides
- **Backend API**: Deployed on Google Cloud Run (see `backend/README.md` for details)

---

## 🤝 Join Our Mission

**Empower and Educate With Purpose**

We believe education should be personalized, accessible, and focused on real-world success. Join our mission to revolutionize how people learn and grow their careers.

### Get Involved

- **Share Your Feedback**: Help us improve by sharing your experience
- **Spread the Word**: Tell others about Edify AI
- **Contribute**: Share resources, tips, and insights with the community
- **Stay Connected**: Follow us for updates and opportunities

---

## 💡 Our Philosophy

### Education for the Real World

Traditional education often fails to prepare students for actual careers. Edify AI bridges that gap by:

- Focusing on skills employers actually want
- Providing real-world practice opportunities
- Connecting learners with opportunities and networks
- Adapting to individual needs and goals
- Making quality education accessible to everyone

### Learning That Adapts to You

We believe learning shouldn't be one-size-fits-all. That's why Edify AI:

- Creates personalized experiences for every user
- Adapts to your pace, style, and goals
- Provides instant feedback and support
- Keeps you engaged and motivated
- Helps you achieve measurable results

---

## 🙏 Acknowledgments

Thank you to all the students, educators, and professionals who have made Edify AI what it is today. Your feedback, participation, and success stories drive us to keep improving.

Special thanks to our global community of **500,000+ learners** who are shaping the future of education.

---

<p align="center">
  <strong>Ready to Transform Your Learning Journey?</strong>
</p>

<p align="center">
  <strong>Empower and Educate With Purpose</strong>
</p>

## 🛠️ Developer & Contributor Guide

If you'd like to contribute, run the app locally, or work on features, here's a compact guide to get started. For more detailed information see the `devops/` and `docs/` folders (CI, testing, performance, and clean builds).

### Tech Stack

**Frontend:**
- **Next.js 14** (App Router) - React framework with server-side rendering
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **Shadcn UI** - High-quality component library
- **Recharts** - Data visualization (bar charts, pie charts, radar charts)
- **Framer Motion** - Smooth animations and transitions
- **tRPC** - End-to-end typesafe APIs
- **React Query** - Server state management
- **Zustand** - Client state management

**Backend:**
- **Python 3.13** - Core backend language
- **LangGraph** - Multi-agent orchestration framework
- **Vertex AI (Gemini 2.0 Flash)** - Google's advanced AI models
- **Pydantic** - Data validation and structured outputs
- **HTTP Server** - Lightweight API server for Cloud Run

**Infrastructure & Deployment:**
- **Google Cloud Platform (GCP)**
  - **Cloud Run** - Serverless container deployment (Backend API)
  - **Vertex AI** - AI/ML model hosting and inference
  - **Cloud Build** - Container image building
  - **Artifact Registry** - Container image storage
- **Neon/PostgreSQL** - Primary database
- **Redis** - Caching and session management
- **Docker** - Containerization
- **GitLab CI/CD** - Continuous integration and deployment

**AI & ML:**
- **Multi-Agent System** - LangGraph-based orchestration
- **Structured Output** - Pydantic models with JSON schema generation
- **Parallel Processing** - Concurrent agent execution
- **Weighted Aggregation** - Intelligent score combination

### Prerequisites

- **Node.js 18+** (we recommend using the same Node version as the Dockerfile)
- **npm 10+** or **yarn**
- **Python 3.13** (for backend development)
- **Docker** (for local container testing)
- **Google Cloud SDK** (for deployment)
- **PostgreSQL** (or Neon account for cloud database)

### Quick Start (Local Development)

**Frontend Setup:**
```bash
# Install dependencies
npm ci --legacy-peer-deps

# Run development server
npm run dev

# Type checking
npm run type-check

# Linting
npm run lint

# Run tests
npm test
```

**Backend Setup:**
```bash
# Navigate to backend directory
cd backend

# Create virtual environment (Python 3.13)
python3.13 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your GCP credentials

# Run local API server
python api_server.py
# Server runs on http://localhost:8000
```

**Environment Variables:**

Frontend (`.env.local`):
```env
PYTHON_BACKEND_URL=http://localhost:8000  # Local development
# PYTHON_BACKEND_URL=https://resume-matcher-api-xxx.run.app  # Production
```

Backend (`.env`):
```env
GOOGLE_CLOUD_PROJECT=your-project-id
VERTEX_AI_LOCATION=us-central1
GEMINI_MODEL_NAME=gemini-2.0-flash-exp
```

### Building for Production

**Frontend:**
```bash
# Build Next.js application
npm run build

# Start production server locally
npm run start
```

**Backend:**
```bash
cd backend

# Build Docker image
docker build -t resume-matcher-api .

# Test locally
docker run --rm -p 8080:8080 \
  -e GOOGLE_CLOUD_PROJECT=your-project \
  -e VERTEX_AI_LOCATION=us-central1 \
  resume-matcher-api
```

### Deployment

**Backend to Cloud Run:**
```bash
cd backend

# Using deployment script
./deploy_cloud_run.sh

# Or manually:
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/resume-matcher-api
gcloud run deploy resume-matcher-api \
  --image gcr.io/$GOOGLE_CLOUD_PROJECT/resume-matcher-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 2 \
  --timeout 300
```

**Frontend Deployment:**
- Configured via GitLab CI/CD pipeline
- Automatically deploys to Cloud Run on `main` branch
- See `devops/PIPELINE.md` for detailed CI/CD configuration

### Architecture Overview

**Multi-Agent Resume Analysis Flow:**
1. **Resume Upload** → Frontend receives PDF/DOCX file
2. **Text Extraction** → Gemini Vision API extracts text from resume
3. **Structured Extraction** → Resume Extractor Agent parses into structured format
4. **Parallel Scoring** → Five specialized agents score different sections simultaneously:
   - Skills Agent
   - Experience Agent
   - Education Agent
   - Projects Agent
   - Meta Agent
5. **Score Aggregation** → Weighted combination of all section scores
6. **Dashboard Display** → Interactive visualizations and recommendations

**System Architecture:**
```
┌─────────────┐
│   Next.js   │  Frontend (React/TypeScript)
│   Frontend  │
└──────┬──────┘
       │ HTTP/API
       ▼
┌─────────────────┐
│  Next.js API    │  /api/resume-analysis
│  Route Handler  │
└──────┬──────────┘
       │ HTTP POST
       ▼
┌─────────────────┐
│  Python Backend │  Cloud Run (Deployed)
│  (LangGraph)    │
│  ┌───────────┐  │
│  │ Orchestrator│ │  Coordinates agents
│  └─────┬─────┘  │
│        │        │
│  ┌─────┴─────┐  │
│  │ 5 Agents │  │  Parallel execution
│  └─────┬─────┘  │
└────────┼────────┘
         │
         ▼
┌─────────────────┐
│   Vertex AI     │  Gemini 2.0 Flash
│   (Gemini)      │
└─────────────────┘
```

### Documentation Index

- `devops/PIPELINE.md` — CI/CD pipeline, GitLab → Cloud Run guidance
- `devops/CLEAN_BUILDS.md` — reproducible build practices and Docker tips
- `devops/TESTING.md` — how to run unit tests, CI test jobs, and coverage
- `docs/SPEED_AND_PERFORMANCE.md` — caching, Inngest workers, tRPC, DB pooling, and profiling
- `docs/ARCHITECTURE.md` — high-level design and system components
- `docs/ENV_SETUP.md` — environment variables and local configuration
- `docs/AGENTIC_WORKFLOWS.md` — AI-driven job workflows and background processing
- `backend/README.md` — Python backend setup and deployment guide
- `backend/QUICK_START.md` — Quick start guide for backend development

### Contributing

Please follow the contribution guidelines in `CONTRIBUTING.md` (code style, PR process, and required checks). All PRs should include:
- Passing type-check (`npm run type-check`)
- Passing lint (`npm run lint`)
- Passing tests (`npm test`)
- Updated documentation if needed

**Backend Contributions:**
- Follow Python PEP 8 style guide
- Use type hints for all functions
- Add docstrings to all modules and functions
- Test locally with `python main_local_test.py`

Thank you to everyone who contributes — your work helps make Edify AI better for learners everywhere.

<p align="center">
  Made with ❤️ by the Edify AI Team
</p>

  ---

  ## 🔌 Model Context Protocol (MCP) Integration

  Edify AI exposes most core product capabilities (courses, pathways, resume analysis, forums, events, internships, AI utilities, transcription, sandboxed code) as **MCP tools** through:

  1. HTTP endpoint: `POST /api/mcp` (App Router) — pass `{ tool: string, input: any }` JSON body.
  2. SDK stdio server: `npx tsx mcp/sdk-server.ts` — provides the same tool set for MCP-compatible clients.

  Heavy or external operations support a `testMode: true` flag to return safe, deterministic stub results (avoiding AI calls, scraping, PDF rendering). This is used extensively in tests.

  ### Auth Parity

  Tools that create/generate substantial content require a `userId` (or nested `user.id`) in input. Missing userId triggers an `ERR_UNAUTHORIZED` error:

  - `course.generate`
  - `pathway.create`

  ### Tool Catalogue

  | Tool | Purpose | Notes |
  |------|---------|-------|
  | course.list | Paginated list of courses | Optional page/limit |
  | course.create | Insert new course metadata | Provide `userInput`, `data` |
  | course.get | Fetch single course | id or courseId |
  | course.update | Patch mutable fields | courseId + patch object |
  | course.delete | Delete a course | id or courseId |
  | course.chapter.get | Get chapter by index | courseId + chapterIndex |
  | course.progress.increment | Increment progress (0-100) | Capped at 100 |
  | course.listByUser | List courses by creator email | email required |
  | course.generate | AI chapter generation & publish | Requires userId; testMode stub |
  | course.chat | Q&A over course chapters | testMode returns stub answer |
  | resume.list | List stored resume analyses | userId + optional limit |
  | resume.analyze | Analyze resume vs job | Returns scores & ATS match |
  | resume.report.get | PDF (base64) for stored analysis | analysisId |
  | resume.report.generate | PDF from provided analysis object | analysis object |
  | forum.topic.list | List forum topics | courseId |
  | forum.topic.create | Create forum topic | courseId, title, content |
  | forum.reply.list | List replies for topic | topicId |
  | forum.reply.create | Create reply | topicId, content |
  | events.list | List hackathons & meetups | includeHackathons/includeMeetups toggles |
  | internships.list | Scraped internships | testMode stub array |
  | pathway.create | Generate learning pathway | Requires userId; testMode stub |
  | pathway.create.personalized | AI market-aware roadmap | Uses Perplexity for market intelligence |
  | pathway.get | Fetch pathway by slug | slug |
  | pathway.list | List all pathways | No input |
  | pathway.progress.update | Update pathway progress | userId, pathwayId, completedSteps |
  | pathway.progress.get | Get user progress | userId, pathwayId |
  | math.solveImage | Solve math from image | imageBase64, testMode stub |
  | ai.generate | Generic Gemini text generation | prompt + optional params |
  | speech.transcribe | Transcribe base64 audio | testMode returns stub segments |
  | code.run | Sandbox code execution (stub) | language, code, testMode |

  ### Sample HTTP Invocation

  ```powershell
  curl -X POST http://localhost:3000/api/mcp -H "Content-Type: application/json" -d '{
    "tool": "ai.generate",
    "input": { "prompt": "Explain async/await simply", "testMode": true }
  }'
  ```

  ### Testing Strategy

  Each tool has targeted Vitest files under `tests/` prefixed with `mcp-` or `mcp-sdk-`. We run only new test files when adding a tool to minimize cycle time. The `testMode` flag ensures deterministic outputs and avoids external dependencies (AI, scraping, PDF generation, sandbox execution).

  ### Adding a New MCP Tool

  1. Implement service logic in `services/` with a `testMode` short-circuit.
  2. Create Zod schemas (or reuse existing) under `app/api/mcp/schemas/`.
  3. Register in `app/api/mcp/registry/index.ts` and `mcp/sdk-server.ts` (manual JSON schema for now).
  4. Add targeted tests (HTTP + SDK) in `tests/`.
  5. Run the new tests only: `npx vitest tests/mcp-<feature>.test.ts tests/mcp-sdk-<feature>.test.ts`.
  6. If auth is required, call `ensureUserId`.

  ### Planned Improvements

  - Zod → JSON Schema auto-generation to remove manual duplication in SDK server.
  - Secure sandbox for `code.run` (container isolation, resource limits).
  - Advanced auth/session integration (beyond simple presence check).

  ---